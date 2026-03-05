import logging
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

async def send_email(to_email: str, subject: str, html_body: str) -> bool:
    """Send an email using AWS SES."""
    client = get_ses_client()
    if not client:
        logger.error("SES client is not configured.")
        return False
        
    sender = settings.AWS_SES_SENDER_EMAIL
    if not sender:
        logger.error("AWS_SES_SENDER_EMAIL is not configured.")
        return False

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [to_email],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': html_body,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=sender,
        )
        logger.info(f"Email sent successfully. Message ID: {response['MessageId']}")
        return True
    except ClientError as e:
        logger.error(f"Failed to send email via SES: {e.response['Error']['Message']}")
        return False

async def send_verification_email(to_email: str, verify_url: str):
    """Sends the email verification link."""
    subject = "Verify Your MemWyre Account"
    body = f"""
    <html>
    <head></head>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>Welcome to MemWyre!</h2>
        <p>Please click the button below to verify your email address and activate your account.</p>
        <p>
            <a href="{verify_url}" style="display: inline-block; padding: 10px 20px; color: white; background-color: #007bff; text-decoration: none; border-radius: 5px;">Verify Email</a>
        </p>
        <br>
        <p>If the button doesn't work, copy and paste this link into your browser:</p>
        <p>{verify_url}</p>
        <p>This link will expire in 24 hours.</p>
    </body>
    </html>
    """
    return await send_email(to_email, subject, body)

async def send_password_reset_email(to_email: str, reset_url: str):
    """Sends the password reset link."""
    subject = "Reset Your MemWyre Password"
    body = f"""
    <html>
    <head></head>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>Password Reset Request</h2>
        <p>We received a request to reset your MemWyre password. Click the button below to set a new password.</p>
        <p>
            <a href="{reset_url}" style="display: inline-block; padding: 10px 20px; color: white; background-color: #007bff; text-decoration: none; border-radius: 5px;">Reset Password</a>
        </p>
        <br>
        <p>If you didn't request a password reset, you can safely ignore this email.</p>
        <p>If the button doesn't work, copy and paste this link into your browser:</p>
        <p>This link will expire in 1 hour.</p>
    </body>
    </html>
    """
    return await send_email(to_email, subject, body)

async def send_otp_email(to_email: str, otp: str):
    """Sends a 6-digit OTP for email verification."""
    subject = "Your MemWyre Verification Code"
    body = f"""
    <html>
    <head></head>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <h2>Verify Your Email</h2>
        <p>Your verification code is:</p>
        <h1 style="color: #007bff; letter-spacing: 5px; font-size: 32px;">{otp}</h1>
        <br>
        <p>This code will expire in 10 minutes.</p>
    </body>
    </html>
    """
    return await send_email(to_email, subject, body)
