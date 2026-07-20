from typing import Optional
import logging

logger = logging.getLogger(__name__)

try:
    import litellm
    # Suppress verbose litellm logs
    litellm.suppress_debug_info = True
    HAVE_LITELLM = True
except ImportError:
    HAVE_LITELLM = False

try:
    import tiktoken
    HAVE_TIKTOKEN = True
except ImportError:
    HAVE_TIKTOKEN = False


class TokenTrackerService:
    def __init__(self):
        # Fallback cost rates per 1M tokens if litellm rate lookup fails
        self.default_rates = {
            "openai": {"in": 2.50, "out": 10.00},
            "azure": {"in": 2.50, "out": 10.00},
            "gemini": {"in": 0.35, "out": 1.05},
            "gcp": {"in": 0.35, "out": 1.05},
            "bedrock": {"in": 3.00, "out": 15.00},
            "anthropic": {"in": 3.00, "out": 15.00},
        }

    def normalize_model(self, provider: Optional[str], model_name: Optional[str]) -> str:
        """
        Normalize model name string into litellm standard identifier.
        """
        model = (model_name or "gpt-4o").strip().lower()
        prov = (provider or "openai").strip().lower()

        if model.startswith("azure/") or model.startswith("bedrock/") or model.startswith("gemini/"):
            return model

        if prov == "azure":
            return f"azure/{model}"
        elif prov in ("bedrock", "aws_bedrock", "aws"):
            if not model.startswith("anthropic.") and not model.startswith("meta.") and not model.startswith("amazon."):
                return f"bedrock/anthropic.{model}"
            return f"bedrock/{model}"
        elif prov in ("gcp", "gemini", "vertex", "google"):
            return model if model.startswith("gemini/") else f"gemini/{model}"
        
        return model

    def count_tokens(self, text: str, provider: str = "openai", model_name: str = "gpt-4o") -> int:
        """
        Calculates exact token count for given text, provider, and model name.
        Uses litellm.token_counter, tiktoken, or accurate heuristic fallback.
        """
        if not text:
            return 0

        target_model = self.normalize_model(provider, model_name)

        if HAVE_LITELLM:
            try:
                return litellm.token_counter(model=target_model, text=text)
            except Exception as e:
                logger.debug(f"litellm token count fallback for {target_model}: {e}")
                # Try bare model name if prefixed provider failed
                try:
                    bare_model = model_name or "gpt-4o"
                    return litellm.token_counter(model=bare_model, text=text)
                except Exception:
                    pass

        if HAVE_TIKTOKEN:
            try:
                encoding = tiktoken.encoding_for_model(model_name or "gpt-4o")
                return len(encoding.encode(text))
            except Exception:
                try:
                    encoding = tiktoken.get_encoding("cl100k_base")
                    return len(encoding.encode(text))
                except Exception:
                    pass

        # Fallback: Approx ~4 chars per token for English/code
        return max(1, len(text) // 4)

    def calculate_cost(
        self,
        tokens_in: int,
        tokens_out: int,
        provider: str = "openai",
        model_name: str = "gpt-4o"
    ) -> float:
        """
        Calculates cost in USD for given input/output tokens, provider, and model.
        """
        if tokens_in <= 0 and tokens_out <= 0:
            return 0.0

        target_model = self.normalize_model(provider, model_name)

        if HAVE_LITELLM:
            try:
                prompt_cost, completion_cost = litellm.cost_per_token(
                    model=target_model,
                    prompt_tokens=tokens_in,
                    completion_tokens=tokens_out
                )
                return round(float(prompt_cost + completion_cost), 6)
            except Exception as e:
                logger.debug(f"litellm cost calculation fallback for {target_model}: {e}")

        # Fallback rates
        prov_key = (provider or "openai").lower()
        rates = self.default_rates.get(prov_key, self.default_rates["openai"])
        
        cost_in = (tokens_in / 1_000_000.0) * rates["in"]
        cost_out = (tokens_out / 1_000_000.0) * rates["out"]
        return round(cost_in + cost_out, 6)


token_tracker = TokenTrackerService()
