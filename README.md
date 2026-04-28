# Memwyre Ecosystem

Welcome to the **Memwyre Ecosystem** repository! This is the public home for all community plugins, extensions, and officially supported integrations for the Memwyre platform.

Here you can find open-source components that extend Memwyre's functionality and allow you to build custom AI workflows.

## 📦 Packages

This repository is structured as a monorepo containing the following packages:

| Package | Description |
|---------|-------------|
| **[`@memwyre/browser-extension`](./packages/browser-extension)** | The official Memwyre browser extension for capturing memories from the web and interacting with ChatGPT. |
| **[`@memwyre/openclaw-plugin`](./packages/openclaw-plugin)** | A plugin for the OpenClaw framework. |
| **[`@memwyre/mcp-server`](./packages/mcp-server)** | The official Model Context Protocol (MCP) server for connecting AI agents directly to your Memwyre vault. |
| **[`@memwyre/client`](./packages/memwyre-client)** | The official Node.js / TypeScript SDK for interacting with the Memwyre REST API. |

## 🚀 Getting Started

### Prerequisites

*   Node.js >= 18
*   Python >= 3.10 (for the MCP server)
*   [pnpm](https://pnpm.io/) (recommended) or npm

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/memwyre/memwyre-ecosystem.git
cd memwyre-ecosystem
npm install
```

## 🤝 Contributing

We welcome contributions! If you're building a new integration, an SDK for a new language, or fixing a bug in an existing plugin, please feel free to open a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
