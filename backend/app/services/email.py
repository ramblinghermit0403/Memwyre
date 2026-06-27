import asyncio
import logging
import functools
import boto3
from botocore.exceptions import ClientError
from app.core.config import settings

logger = logging.getLogger(__name__)


def get_ses_client():
    if not settings.AWS_ACCESS_KEY_ID or not settings.AWS_SECRET_ACCESS_KEY:
        logger.warning("AWS credentials not set. Email service disabled.")
        return None

    return boto3.client(
        'ses',
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )


def _send_email_sync(to_email: str, subject: str, html_body: str, sender: str) -> bool:
    """Synchronous SES send — runs in a thread executor."""
    client = get_ses_client()
    if not client:
        logger.error("SES client is not configured.")
        return False

    try:
        response = client.send_email(
            Destination={'ToAddresses': [to_email]},
            Message={
                'Body': {'Html': {'Charset': "UTF-8", 'Data': html_body}},
                'Subject': {'Charset': "UTF-8", 'Data': subject},
            },
            Source=sender,
        )
        logger.info(f"Email sent successfully to {to_email}. Message ID: {response['MessageId']}")
        return True
    except ClientError as e:
        logger.error(f"Failed to send email via SES to {to_email}: {e.response['Error']['Message']}")
        return False


async def send_email(to_email: str, subject: str, html_body: str) -> bool:
    """Send an email using AWS SES (non-blocking async wrapper)."""
    base_sender = settings.AWS_SES_SENDER_EMAIL
    if not base_sender:
        logger.error("AWS_SES_SENDER_EMAIL is not configured.")
        return False
        
    sender = f"Memwyre <{base_sender}>"

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None,
        functools.partial(_send_email_sync, to_email, subject, html_body, sender)
    )


async def send_verification_email(to_email: str, verify_url: str):
    """Sends the email verification link."""
    subject = "Verify Your Memwyre Account"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 40px 20px; }}
            .card {{ background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04); border: 1px solid #f0f0f0; }}
            .header {{ padding: 32px 40px; text-align: center; border-bottom: 1px solid #f5f5f5; }}
            .logo {{ font-size: 22px; font-weight: 700; color: #111; margin: 0; display: inline-block; text-align: center; }}
            .logo img {{ height: 28px; width: auto; vertical-align: middle; margin-right: 12px; position: relative; top: -2px; }}
            .content {{ padding: 40px; text-align: center; }}
            .title {{ margin: 0 0 16px; font-size: 22px; font-weight: 700; color: #111; }}
            .text {{ margin: 0 0 32px; font-size: 16px; line-height: 1.6; color: #555; text-align: left; }}
            .btn-wrap {{ text-align: center; margin: 40px 0; }}
            .btn {{ display: inline-block; padding: 16px 36px; background-color: #D97757; color: #ffffff; text-decoration: none; border-radius: 12px; font-size: 16px; font-weight: 600; box-shadow: 0 4px 12px rgba(217, 119, 87, 0.25); text-align: center; }}
            .footer {{ padding: 32px 40px; background-color: #fafafa; text-align: center; border-top: 1px solid #eee; }}
            .footer-text {{ margin: 0; font-size: 13px; color: #888; line-height: 1.5; }}
            .fallback {{ margin-top: 32px; font-size: 13px; color: #888; text-align: left; padding: 16px; background: #f9f9f9; border-radius: 8px; }}
            .fallback-link {{ color: #D97757; word-break: break-all; margin-top: 4px; display: block; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <div class="header">
                    <div class="logo">
                        <img src="https://memwyre.tech/image.svg" alt="Memwyre Logo" />
                        <span>Memwyre</span>
                    </div>
                </div>
                <div class="content">
                    <h2 class="title">Verify your email address</h2>
                    <p class="text">You're almost there! We just need to verify your email address before you can start organizing your AI interactions.</p>
                    
                    <div class="btn-wrap">
                        <a href="{verify_url}" class="btn">Verify your email</a>
                    </div>
                    
                    <div class="fallback">
                        If the button doesn't work, copy and paste this link into your browser:
                        <a href="{verify_url}" class="fallback-link">{verify_url}</a>
                    </div>
                </div>
                <div class="footer">
                    <p class="footer-text">If you didn't create an account, you can safely ignore this email.</p>
                    <p class="footer-text" style="margin-top: 12px;">© Memwyre. All rights reserved.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return await send_email(to_email, subject, body)


async def send_password_reset_email(to_email: str, reset_url: str):
    """Sends the password reset link."""
    subject = "Reset Your Memwyre Password"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 40px 20px; }}
            .card {{ background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04); border: 1px solid #f0f0f0; }}
            .header {{ padding: 32px 40px; text-align: center; border-bottom: 1px solid #f5f5f5; }}
            .logo {{ font-size: 22px; font-weight: 700; color: #111; margin: 0; display: inline-block; text-align: center; }}
            .logo img {{ height: 28px; width: auto; vertical-align: middle; margin-right: 12px; position: relative; top: -2px; }}
            .content {{ padding: 40px; text-align: center; }}
            .title {{ margin: 0 0 16px; font-size: 22px; font-weight: 700; color: #111; }}
            .text {{ margin: 0 0 32px; font-size: 16px; line-height: 1.6; color: #555; text-align: left; }}
            .btn-wrap {{ text-align: center; margin: 40px 0; }}
            .btn {{ display: inline-block; padding: 16px 36px; background-color: #111; color: #ffffff; text-decoration: none; border-radius: 12px; font-size: 16px; font-weight: 600; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15); text-align: center; }}
            .footer {{ padding: 32px 40px; background-color: #fafafa; text-align: center; border-top: 1px solid #eee; }}
            .footer-text {{ margin: 0; font-size: 13px; color: #888; line-height: 1.5; }}
            .fallback {{ margin-top: 32px; font-size: 13px; color: #888; text-align: left; padding: 16px; background: #f9f9f9; border-radius: 8px; }}
            .fallback-link {{ color: #D97757; word-break: break-all; margin-top: 4px; display: block; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <div class="header">
                    <div class="logo">
                        <img src="https://memwyre.tech/image.svg" alt="Memwyre Logo" />
                        <span>Memwyre</span>
                    </div>
                </div>
                <div class="content">
                    <h2 class="title">Reset your password</h2>
                    <p class="text">We received a request to reset the password for your Memwyre account. Click the button below to choose a new password.</p>
                    
                    <div class="btn-wrap">
                        <a href="{reset_url}" class="btn">Reset Password</a>
                    </div>
                    
                    <div class="fallback">
                        If the button doesn't work, copy and paste this link into your browser:
                        <a href="{reset_url}" class="fallback-link">{reset_url}</a>
                    </div>
                </div>
                <div class="footer">
                    <p class="footer-text">If you didn't request a password reset, you can safely ignore this email. Your password will remain unchanged.</p>
                    <p class="footer-text" style="margin-top: 12px;">© Memwyre. All rights reserved.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return await send_email(to_email, subject, body)


async def send_otp_email(to_email: str, otp: str):
    """Sends a 6-digit OTP for email verification."""
    subject = f"Your Memwyre verification code is {otp}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 40px 20px; }}
            .card {{ background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04); border: 1px solid #f0f0f0; }}
            .header {{ padding: 32px 40px; text-align: center; border-bottom: 1px solid #f5f5f5; }}
            .logo {{ font-size: 22px; font-weight: 700; color: #111; margin: 0; display: inline-block; text-align: center; }}
            .logo img {{ height: 28px; width: auto; vertical-align: middle; margin-right: 12px; position: relative; top: -2px; }}
            .content {{ padding: 40px 40px 60px; text-align: center; }}
            .title {{ margin: 0 0 16px; font-size: 22px; font-weight: 700; color: #111; }}
            .text {{ margin: 0 0 40px; font-size: 16px; line-height: 1.6; color: #555; text-align: center; }}
            .otp-box {{ background-color: #FFF5F1; border: 2px dashed #EBC4B6; border-radius: 16px; padding: 32px; margin: 0 auto; max-width: 320px; }}
            .otp-code {{ font-size: 42px; font-weight: 800; letter-spacing: 12px; margin-right: -12px; color: #D97757; margin-bottom: 0; margin-top: 0; display: block; }}
            .footer {{ padding: 32px 40px; background-color: #fafafa; text-align: center; border-top: 1px solid #eee; }}
            .footer-text {{ margin: 0; font-size: 13px; color: #888; line-height: 1.5; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <div class="header">
                    <div class="logo">
                        <img src="https://memwyre.tech/image.svg" alt="Memwyre Logo" />
                        <span>Memwyre</span>
                    </div>
                </div>
                <div class="content">
                    <h2 class="title">Confirm your email address</h2>
                    <p class="text">Please enter the following verification code to complete your sign-in process. This code will expire in 10 minutes.</p>
                    
                    <div class="otp-box">
                        <h1 class="otp-code">{otp}</h1>
                    </div>
                </div>
                <div class="footer">
                    <p class="footer-text">Didn't request this? Please ignore this message.</p>
                    <p class="footer-text" style="margin-top: 12px;">© Memwyre. All rights reserved.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return await send_email(to_email, subject, body)


async def send_welcome_email(to_email: str, name: str):
    """Sends a welcome email to a new verified user."""
    subject = "Welcome to Memwyre"
    display_name = name if name else "there"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 40px 20px; }}
            .card {{ background-color: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04); border: 1px solid #f0f0f0; }}
            .header {{ padding: 32px 40px; text-align: center; border-bottom: 1px solid #f5f5f5; }}
            .logo {{ font-size: 22px; font-weight: 700; color: #111; margin: 0; display: inline-block; text-align: center; }}
            .logo img {{ height: 28px; width: auto; vertical-align: middle; margin-right: 12px; position: relative; top: -2px; }}
            .content {{ padding: 40px; text-align: left; }}
            .title {{ margin: 0 0 24px; font-size: 24px; font-weight: 700; color: #111; letter-spacing: -0.5px; }}
            .text {{ margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #444; }}
            .feature-list {{ margin: 32px 0; padding: 0 0 0 16px; list-style: none; border-left: 2px solid #EBC4B6; }}
            .feature-item {{ margin-bottom: 16px; position: relative; }}
            .feature-item::before {{ content: ''; position: absolute; left: -21px; top: 10px; width: 8px; height: 8px; background-color: #D97757; border-radius: 50%; border: 2px solid #fff; box-sizing: border-box; }}
            .feature-content h4 {{ margin: 0; font-size: 16px; font-weight: 500; color: #222; }}
            .tip-box {{ background-color: #FFF5F1; border-radius: 12px; padding: 24px; margin: 32px 0; border: 1px solid #FFE7DF; }}
            .tip-box p {{ margin: 0; font-size: 15px; color: #D97757; line-height: 1.6; }}
            .signoff {{ margin-top: 40px; font-size: 16px; color: #111; font-weight: 600; line-height: 1.5; }}
            .btn-wrap {{ text-align: center; margin: 40px 0 24px; }}
            .btn {{ display: inline-block; padding: 16px 40px; background-color: #D97757; color: #ffffff; text-decoration: none; border-radius: 12px; font-size: 16px; font-weight: 600; box-shadow: 0 4px 16px rgba(217, 119, 87, 0.25); text-align: center; }}
            .footer {{ padding: 32px 40px; background-color: #fafafa; text-align: center; border-top: 1px solid #eee; }}
            .footer-text {{ margin: 0; font-size: 13px; color: #888; line-height: 1.5; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <div class="header">
                    <div class="logo">
                        <img src="https://memwyre.tech/image.svg" alt="Memwyre Logo" />
                        <span>Memwyre</span>
                    </div>
                </div>
                <div class="content">
                    <h2 class="title">Hi {display_name}, <br/>Welcome to Memwyre 👋</h2>
                    <p class="text">We're excited to have you on board.</p>
                    <p class="text">Memwyre is built to solve a simple but frustrating problem — the information you save across tools, chats, and tabs gets lost when you actually need it. Memwyre acts as your second brain, helping you instantly recall, connect, and use your knowledge when it matters most.</p>
                    
                    <p class="text"><strong>Here's what you can do right away:</strong></p>
                    <ul class="feature-list">
                        <li class="feature-item">
                            <div class="feature-content">
                                <h4>Capture insights from anywhere (tabs, chats, docs)</h4>
                            </div>
                        </li>
                        <li class="feature-item">
                            <div class="feature-content">
                                <h4>Retrieve anything with natural language</h4>
                            </div>
                        </li>
                        <li class="feature-item">
                            <div class="feature-content">
                                <h4>Connect ideas across time and context</h4>
                            </div>
                        </li>
                        <li class="feature-item">
                            <div class="feature-content">
                                <h4>Never lose important information again</h4>
                            </div>
                        </li>
                    </ul>

                    <div class="tip-box">
                        <p><strong>💡 Quick tip:</strong> Start by saving something you'll need later — a link, a note, or a conversation. Then try asking Memwyre for it in your own words.</p>
                    </div>

                    <p class="text">We're just getting started, and your feedback will shape what comes next. If something feels missing or could be better, we'd love to hear from you.</p>

                    <p class="text">Welcome to a smarter way of remembering.</p>
                    
                    <div class="btn-wrap">
                        <a href="https://memwyre.tech/login" class="btn" style="color: #ffffff; text-decoration: none;">Log in to Memwyre</a>
                    </div>
                    
                    <div class="signoff">
                        Himansh Shivhare <br/>
                        <span style="font-weight: 400; color: #666;">Memwyre</span>
                    </div>
                </div>
                <div class="footer">
                    <p class="footer-text">© Memwyre. All rights reserved.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return await send_email(to_email, subject, body)
