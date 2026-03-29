Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing

$CanvasWidth = 1280
$CanvasHeight = 800

function New-ColorFromHex {
    param(
        [Parameter(Mandatory = $true)][string]$Hex,
        [int]$Alpha = 255
    )
    $clean = $Hex.Trim().TrimStart("#")
    if ($clean.Length -ne 6) {
        throw "Invalid hex color: $Hex"
    }
    $r = [Convert]::ToInt32($clean.Substring(0, 2), 16)
    $g = [Convert]::ToInt32($clean.Substring(2, 2), 16)
    $b = [Convert]::ToInt32($clean.Substring(4, 2), 16)
    return [System.Drawing.Color]::FromArgb($Alpha, $r, $g, $b)
}

function New-RoundedRectPath {
    param(
        [float]$X,
        [float]$Y,
        [float]$Width,
        [float]$Height,
        [float]$Radius
    )
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $diameter = $Radius * 2
    if ($Radius -le 0) {
        $path.AddRectangle([System.Drawing.RectangleF]::new($X, $Y, $Width, $Height))
        return $path
    }
    $path.AddArc($X, $Y, $diameter, $diameter, 180, 90)
    $path.AddArc($X + $Width - $diameter, $Y, $diameter, $diameter, 270, 90)
    $path.AddArc($X + $Width - $diameter, $Y + $Height - $diameter, $diameter, $diameter, 0, 90)
    $path.AddArc($X, $Y + $Height - $diameter, $diameter, $diameter, 90, 90)
    $path.CloseFigure()
    return $path
}

function Draw-RoundedPanel {
    param(
        [System.Drawing.Graphics]$Graphics,
        [float]$X,
        [float]$Y,
        [float]$Width,
        [float]$Height,
        [float]$Radius,
        [System.Drawing.Color]$FillColor,
        [System.Drawing.Color]$BorderColor,
        [float]$BorderWidth = 1
    )
    $path = New-RoundedRectPath -X $X -Y $Y -Width $Width -Height $Height -Radius $Radius
    $fillBrush = New-Object System.Drawing.SolidBrush($FillColor)
    $borderPen = New-Object System.Drawing.Pen($BorderColor, $BorderWidth)
    $Graphics.FillPath($fillBrush, $path)
    $Graphics.DrawPath($borderPen, $path)
    $fillBrush.Dispose()
    $borderPen.Dispose()
    $path.Dispose()
}

function Draw-Glow {
    param(
        [System.Drawing.Graphics]$Graphics,
        [float]$CenterX,
        [float]$CenterY,
        [float]$Radius,
        [System.Drawing.Color]$GlowColor
    )
    for ($i = 14; $i -ge 1; $i--) {
        $ratio = $i / 14.0
        $alpha = [int](22 * $ratio * $ratio)
        if ($alpha -le 0) {
            continue
        }
        $currentRadius = $Radius * $ratio
        $brush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb($alpha, $GlowColor.R, $GlowColor.G, $GlowColor.B))
        $Graphics.FillEllipse($brush, $CenterX - $currentRadius, $CenterY - $currentRadius, $currentRadius * 2, $currentRadius * 2)
        $brush.Dispose()
    }
}

function Draw-BackgroundDots {
    param(
        [System.Drawing.Graphics]$Graphics,
        [int]$Width,
        [int]$Height,
        [hashtable]$Colors
    )
    $spacing = 28
    $primaryBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(44, $Colors.highlight.R, $Colors.highlight.G, $Colors.highlight.B))
    $secondaryBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(30, $Colors.accent.R, $Colors.accent.G, $Colors.accent.B))

    for ($y = -16; $y -le ($Height + 16); $y += $spacing) {
        $row = [int](($y + 16) / $spacing)
        $offset = if (($row % 2) -eq 0) { 0 } else { [int]($spacing / 2) }

        for ($x = -16; $x -le ($Width + 16); $x += $spacing) {
            $dotX = $x + $offset
            $pickPrimary = (([int](($x + 16) / $spacing) + $row) % 3) -eq 0
            $dotSize = if ($pickPrimary) { 2.8 } else { 2.0 }
            $brush = if ($pickPrimary) { $primaryBrush } else { $secondaryBrush }
            $Graphics.FillEllipse($brush, $dotX, $y, $dotSize, $dotSize)
        }
    }

    $primaryBrush.Dispose()
    $secondaryBrush.Dispose()
}

function Draw-ImageContain {
    param(
        [System.Drawing.Graphics]$Graphics,
        [System.Drawing.Image]$Image,
        [float]$X,
        [float]$Y,
        [float]$Width,
        [float]$Height,
        [float]$Padding = 0
    )
    $innerX = $X + $Padding
    $innerY = $Y + $Padding
    $innerW = $Width - (2 * $Padding)
    $innerH = $Height - (2 * $Padding)
    if ($innerW -le 0 -or $innerH -le 0) {
        return
    }
    $scale = [Math]::Min($innerW / $Image.Width, $innerH / $Image.Height)
    $drawW = $Image.Width * $scale
    $drawH = $Image.Height * $scale
    $drawX = $innerX + (($innerW - $drawW) / 2)
    $drawY = $innerY + (($innerH - $drawH) / 2)
    $Graphics.DrawImage($Image, [System.Drawing.RectangleF]::new($drawX, $drawY, $drawW, $drawH))
}

function Get-ImageFitNoUpscale {
    param(
        [System.Drawing.Image]$Image,
        [float]$Width,
        [float]$Height
    )
    if ($Width -le 0 -or $Height -le 0 -or $Image.Width -le 0 -or $Image.Height -le 0) {
        return @{
            w = 0
            h = 0
        }
    }
    $scale = [Math]::Min(1.0, [Math]::Min($Width / $Image.Width, $Height / $Image.Height))
    return @{
        w = $Image.Width * $scale
        h = $Image.Height * $scale
    }
}

function Draw-SnapshotCard {
    param(
        [System.Drawing.Graphics]$Graphics,
        [string]$ImagePath,
        [hashtable]$Rect,
        [hashtable]$Colors,
        [hashtable]$Secondary
    )
    $img = [System.Drawing.Image]::FromFile($ImagePath)
    $fit = Get-ImageFitNoUpscale -Image $img -Width $Rect.w -Height $Rect.h
    if ($fit.w -le 0 -or $fit.h -le 0) {
        $img.Dispose()
        return
    }
    $mainX = $Rect.x + (($Rect.w - $fit.w) / 2.0)
    $mainY = $Rect.y + (($Rect.h - $fit.h) / 2.0)

    $shadowPath = New-RoundedRectPath -X ($mainX + 8) -Y ($mainY + 10) -Width $fit.w -Height $fit.h -Radius 24
    $shadowBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(72, 0, 0, 0))
    $Graphics.FillPath($shadowBrush, $shadowPath)
    $shadowBrush.Dispose()
    $shadowPath.Dispose()

    $mainPath = New-RoundedRectPath -X $mainX -Y $mainY -Width $fit.w -Height $fit.h -Radius 24
    $graphicsState = $Graphics.Save()
    $Graphics.SetClip($mainPath)
    $Graphics.DrawImage($img, [System.Drawing.RectangleF]::new($mainX, $mainY, $fit.w, $fit.h))
    $Graphics.Restore($graphicsState)
    $imageBorderPen = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(64, 255, 255, 255), 1.25)
    $Graphics.DrawPath($imageBorderPen, $mainPath)
    $imageBorderPen.Dispose()
    $mainPath.Dispose()

    if ($Secondary) {
        $dest = $Secondary.dest
        $crop = $Secondary.crop

        $secShadowPath = New-RoundedRectPath -X ($dest[0] + 6) -Y ($dest[1] + 8) -Width $dest[2] -Height $dest[3] -Radius 18
        $secShadowBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(68, 0, 0, 0))
        $Graphics.FillPath($secShadowBrush, $secShadowPath)
        $secShadowBrush.Dispose()
        $secShadowPath.Dispose()

        Draw-RoundedPanel -Graphics $Graphics -X $dest[0] -Y $dest[1] -Width $dest[2] -Height $dest[3] -Radius 18 -FillColor $Colors.surface -BorderColor $Colors.border -BorderWidth 2
        $innerPad = 10
        $drawX = [int]($dest[0] + $innerPad)
        $drawY = [int]($dest[1] + $innerPad)
        $drawW = [int]($dest[2] - (2 * $innerPad))
        $drawH = [int]($dest[3] - (2 * $innerPad))
        $destRect = [System.Drawing.Rectangle]::new($drawX, $drawY, $drawW, $drawH)
        $Graphics.DrawImage($img, $destRect, $crop[0], $crop[1], $crop[2], $crop[3], [System.Drawing.GraphicsUnit]::Pixel)
    }

    $img.Dispose()
}

function Draw-AdditionalCards {
    param(
        [System.Drawing.Graphics]$Graphics,
        [object[]]$Cards,
        [string]$SourceDir,
        [hashtable]$Colors
    )
    if (-not $Cards) {
        return
    }

    foreach ($card in $Cards) {
        $cardImagePath = Join-Path $SourceDir $card.image
        if (-not (Test-Path $cardImagePath)) {
            throw "Missing additional image: '$cardImagePath'."
        }
        Assert-ValidSourceImage -ImagePath $cardImagePath -SlideId ("extra-" + $card.image)
        Draw-SnapshotCard -Graphics $Graphics -ImagePath $cardImagePath -Rect $card.rect -Colors $Colors -Secondary $null
    }
}

function Draw-BrandAnchors {
    param(
        [System.Drawing.Graphics]$Graphics,
        [string]$LogoPath,
        [hashtable]$Colors
    )
    return
}

function Draw-SlideText {
    param(
        [System.Drawing.Graphics]$Graphics,
        [string]$Headline,
        [string]$SupportLine,
        [float]$X,
        [float]$Y,
        [float]$Width,
        [hashtable]$Colors,
        [string]$HeadlineIconPath = $null,
        [float]$SupportOffset = 4
    )
    $headlineFont = New-Object System.Drawing.Font("Segoe UI Bold", 72, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $bodyFont = New-Object System.Drawing.Font("Segoe UI Semibold", 38, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)

    $headlineBrush = New-Object System.Drawing.SolidBrush($Colors.textPrimary)
    $bodyBrush = New-Object System.Drawing.SolidBrush($Colors.textSecondary)

    $stringFormat = New-Object System.Drawing.StringFormat
    $stringFormat.Trimming = [System.Drawing.StringTrimming]::Word
    $stringFormat.FormatFlags = [System.Drawing.StringFormatFlags]::LineLimit

    $headlineHeight = 0
    $logoToken = "[logo]"
    if (
        $Headline.Contains($logoToken) -and
        -not [string]::IsNullOrWhiteSpace($HeadlineIconPath) -and
        (Test-Path $HeadlineIconPath)
    ) {
        $tokenIndex = $Headline.IndexOf($logoToken)
        $leftPart = $Headline.Substring(0, $tokenIndex)
        $rightPart = $Headline.Substring($tokenIndex + $logoToken.Length)
        $leftRender = $leftPart.TrimEnd()

        $leftSize = $Graphics.MeasureString($leftRender, $headlineFont)
        $leftWrappedSize = $Graphics.MeasureString($leftRender, $headlineFont, [int]$Width)
        $leftRect = [System.Drawing.RectangleF]::new($X, $Y, $Width, 180)
        $Graphics.DrawString($leftRender, $headlineFont, $headlineBrush, $leftRect, $stringFormat)

        $iconSize = 64.0
        $iconPad = 2.0
        $iconX = $X + [Math]::Ceiling($leftSize.Width) + $iconPad
        $iconY = $Y + 12
        $icon = [System.Drawing.Image]::FromFile($HeadlineIconPath)
        $Graphics.DrawImage($icon, [System.Drawing.RectangleF]::new($iconX, $iconY, $iconSize, $iconSize))
        $icon.Dispose()

        if (-not [string]::IsNullOrWhiteSpace($rightPart)) {
            $rightX = $iconX + $iconSize + $iconPad
            $rightRect = [System.Drawing.RectangleF]::new($rightX, $Y, $Width - ($rightX - $X), 180)
            $Graphics.DrawString($rightPart, $headlineFont, $headlineBrush, $rightRect, $stringFormat)
        }

        $headlineHeight = [Math]::Max([Math]::Ceiling($leftWrappedSize.Height), [Math]::Ceiling($iconSize + 14))
    } else {
        $headlineRect = [System.Drawing.RectangleF]::new($X, $Y, $Width, 330)
        $Graphics.DrawString($Headline, $headlineFont, $headlineBrush, $headlineRect, $stringFormat)
        $headlineMeasured = $Graphics.MeasureString($Headline, $headlineFont, [int]$Width)
        $headlineHeight = [Math]::Ceiling($headlineMeasured.Height)
    }

    $supportY = $Y + $headlineHeight + $SupportOffset
    $supportRect = [System.Drawing.RectangleF]::new($X, $supportY, $Width, 240)
    $Graphics.DrawString($SupportLine, $bodyFont, $bodyBrush, $supportRect, $stringFormat)

    $stringFormat.Dispose()
    $headlineBrush.Dispose()
    $bodyBrush.Dispose()
    $headlineFont.Dispose()
    $bodyFont.Dispose()
}

function Draw-TitleOnlyLines {
    param(
        [System.Drawing.Graphics]$Graphics,
        [string[]]$Lines,
        [float]$X,
        [float]$Y,
        [float]$Width,
        [hashtable]$Colors,
        [string]$HeadlineIconPath = $null,
        [string]$SupportLine = "",
        [float]$SupportOffset = 0,
        [float]$HeadlineFontSize = 58,
        [float]$BodyFontSize = 38,
        [float]$LineAdvance = 82
    )
    $headlineFont = New-Object System.Drawing.Font("Segoe UI Bold", $HeadlineFontSize, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $bodyFont = New-Object System.Drawing.Font("Segoe UI Semibold", $BodyFontSize, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
    $headlineBrush = New-Object System.Drawing.SolidBrush($Colors.textPrimary)
    $bodyBrush = New-Object System.Drawing.SolidBrush($Colors.textSecondary)
    $stringFormat = New-Object System.Drawing.StringFormat
    $stringFormat.Trimming = [System.Drawing.StringTrimming]::Word
    $stringFormat.FormatFlags = [System.Drawing.StringFormatFlags]::LineLimit

    $cursorY = $Y
    $logoToken = "[logo]"

    foreach ($line in $Lines) {
        if (
            $line.Contains($logoToken) -and
            -not [string]::IsNullOrWhiteSpace($HeadlineIconPath) -and
            (Test-Path $HeadlineIconPath)
        ) {
            $tokenIndex = $line.IndexOf($logoToken)
            $leftPart = $line.Substring(0, $tokenIndex).TrimEnd()
            $rightPart = $line.Substring($tokenIndex + $logoToken.Length).TrimStart()

            $leftSize = if ([string]::IsNullOrWhiteSpace($leftPart)) {
                [System.Drawing.SizeF]::new(0, 0)
            } else {
                $Graphics.MeasureString($leftPart, $headlineFont)
            }

            $iconSize = [Math]::Round($HeadlineFontSize * 0.86, 2)
            $iconPad = 6.0
            if (-not [string]::IsNullOrWhiteSpace($leftPart)) {
                $Graphics.DrawString($leftPart, $headlineFont, $headlineBrush, [System.Drawing.PointF]::new($X, $cursorY))
            }

            $iconX = $X + $leftSize.Width + $iconPad
            $iconY = $cursorY + [Math]::Max(6, [Math]::Round($HeadlineFontSize * 0.18, 2))
            $icon = [System.Drawing.Image]::FromFile($HeadlineIconPath)
            $Graphics.DrawImage($icon, [System.Drawing.RectangleF]::new($iconX, $iconY, $iconSize, $iconSize))
            $icon.Dispose()

            if (-not [string]::IsNullOrWhiteSpace($rightPart)) {
                $rightX = $iconX + $iconSize + $iconPad
                $Graphics.DrawString($rightPart, $headlineFont, $headlineBrush, [System.Drawing.PointF]::new($rightX, $cursorY))
            }
        } else {
            $Graphics.DrawString($line, $headlineFont, $headlineBrush, [System.Drawing.PointF]::new($X, $cursorY))
        }

        $cursorY += $LineAdvance
    }

    if (-not [string]::IsNullOrWhiteSpace($SupportLine)) {
        $supportY = $cursorY + $SupportOffset
        $supportRect = [System.Drawing.RectangleF]::new($X, $supportY, $Width, 240)
        $Graphics.DrawString($SupportLine, $bodyFont, $bodyBrush, $supportRect, $stringFormat)
    }

    $stringFormat.Dispose()
    $bodyBrush.Dispose()
    $headlineBrush.Dispose()
    $bodyFont.Dispose()
    $headlineFont.Dispose()
}

function New-SlideCanvas {
    param(
        [int]$Width,
        [int]$Height,
        [hashtable]$Colors
    )
    $bitmap = New-Object System.Drawing.Bitmap($Width, $Height, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

    $gradientBrush = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
        [System.Drawing.Point]::new(0, 0),
        [System.Drawing.Point]::new($Width, $Height),
        $Colors.bgStart,
        $Colors.bgEnd
    )
    $graphics.FillRectangle($gradientBrush, 0, 0, $Width, $Height)
    $gradientBrush.Dispose()

    Draw-BackgroundDots -Graphics $graphics -Width $Width -Height $Height -Colors $Colors
    Draw-Glow -Graphics $graphics -CenterX 1060 -CenterY 120 -Radius 260 -GlowColor $Colors.accent
    Draw-Glow -Graphics $graphics -CenterX 260 -CenterY 680 -Radius 320 -GlowColor $Colors.highlight

    return @{
        bitmap = $bitmap
        graphics = $graphics
    }
}

function New-PromoTile {
    param(
        [string]$OutputPath,
        [string]$LogoPath,
        [hashtable]$Colors
    )
    $tile = New-SlideCanvas -Width 440 -Height 280 -Colors $Colors
    $bitmap = $tile.bitmap
    $graphics = $tile.graphics

    $logo = [System.Drawing.Image]::FromFile($LogoPath)
    Draw-ImageContain -Graphics $graphics -Image $logo -X 152 -Y 34 -Width 136 -Height 136
    $logo.Dispose()

    $nameFont = New-Object System.Drawing.Font("Segoe UI Bold", 34, [System.Drawing.FontStyle]::Bold, [System.Drawing.GraphicsUnit]::Pixel)
    $taglineFont = New-Object System.Drawing.Font("Segoe UI Semibold", 18, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
    $nameBrush = New-Object System.Drawing.SolidBrush($Colors.textPrimary)
    $taglineBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(220, $Colors.textSecondary.R, $Colors.textSecondary.G, $Colors.textSecondary.B))

    $format = New-Object System.Drawing.StringFormat
    $format.Alignment = [System.Drawing.StringAlignment]::Center
    $format.LineAlignment = [System.Drawing.StringAlignment]::Near

    $graphics.DrawString("MemWyre", $nameFont, $nameBrush, [System.Drawing.RectangleF]::new(40, 174, 360, 44), $format)
    $graphics.DrawString("", $taglineFont, $taglineBrush, [System.Drawing.RectangleF]::new(38, 220, 364, 28), $format)

    $format.Dispose()
    $nameBrush.Dispose()
    $taglineBrush.Dispose()
    $nameFont.Dispose()
    $taglineFont.Dispose()

    $bitmap.Save($OutputPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $graphics.Dispose()
    $bitmap.Dispose()
}

$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot "..\..\"))
$assetsDir = Join-Path $repoRoot "frontend\src\assets"
$sourceDir = Join-Path $assetsDir "extension_graphics_sources"
$outputDir = Join-Path $assetsDir "extension_graphics"
if (-not (Test-Path $sourceDir)) {
    New-Item -Path $sourceDir -ItemType Directory | Out-Null
}

function Assert-ValidSourceImage {
    param(
        [string]$ImagePath,
        [string]$SlideId
    )
    $img = $null
    try {
        $img = [System.Drawing.Image]::FromFile($ImagePath)

        # Generated slides are always export-sized. Reject them as inputs so we
        # never accidentally re-feed outputs back into the pipeline.
        if ($img.Width -eq $CanvasWidth -and $img.Height -eq $CanvasHeight) {
            throw "Invalid source image for '$SlideId': '$ImagePath' is ${CanvasWidth}x${CanvasHeight}, which matches the generated slide size. Use the original raw snapshot instead of an exported slide."
        }
    }
    finally {
        if ($img) {
            $img.Dispose()
        }
    }
}
if (-not (Test-Path $outputDir)) {
    New-Item -Path $outputDir -ItemType Directory | Out-Null
}
if ([System.IO.Path]::GetFullPath($sourceDir).Equals([System.IO.Path]::GetFullPath($outputDir), [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Invalid configuration: source and output directories must be different."
}

$colors = @{
    bgStart      = New-ColorFromHex -Hex "#1A1918"
    bgEnd        = New-ColorFromHex -Hex "#24211F"
    surface      = New-ColorFromHex -Hex "#2D2B2A"
    border       = New-ColorFromHex -Hex "#FFFFFF" -Alpha 26
    textPrimary  = New-ColorFromHex -Hex "#FFFFFF"
    textSecondary= New-ColorFromHex -Hex "#F2EEE8"
    accent       = New-ColorFromHex -Hex "#D97757"
    highlight    = New-ColorFromHex -Hex "#E8956E"
}

$logoPath = Join-Path $repoRoot "extension\logo.png"

$slides = @(
    @{
        id = "01-capture-button"
        headline = "Save AI responses and prompts with the [logo] button"
        support = ""
        layout = "right"
        image = "save_btn_2.png"

        primaryRect = @{ x = 180; y = 300; w = 648; h = 540 }
        textRect = @{ x = 78; y = 164; w = 430 }
        headlineLines = @("Save AI responses", "and prompts with", "the [logo] button")
        headlineIcon = "extension\\logo.png"
        supportOffset = 4
        extraCards = @(
            @{
                image = "save_button.png"
                rect = @{ x = 580; y = 90; w = 648; h = 540 }
            }
        )
        secondary = $null
    },
    @{
        id = "02-sync-button"
        headline = "Tap [logo] button to Sync your captured context to your knowledge base."
        support = ""
        image = "sync button.png"
        layout = "left"
        primaryRect = @{ x = 50; y = 30; w = 648; h = 540 }
        textRect = @{ x = 748; y = 156; w = 432 }
        headlineLines = @("Tap [logo] button", "to sync your", "context to your", "knowledge base.")
        headlineIcon = "extension\\logo.png"
        supportOffset = -8
        extraCards = @(
            @{
                image = "sync_btn.png"
                rect = @{ x = 350; y = 460; w = 720; h = 304 }
            }
        )
        secondary = $null
    },
    @{
        id = "03-mcp-server-connections"
        headline = "Connect your AI stack with MCP."
        support = "Use your memory from Cursor, Claude, VS Code, and more."
        image = "mcp_connections.png"
        layout = "right"
        primaryRect = @{ x = 566; y = 168; w = 648; h = 540 }
        textRect = @{ x = 78; y = 164; w = 430 }
        supportOffset = -10
        secondary = $null
    },
    @{
        id = "04-save-from-any-webpage"
        headline = "Save from any webpage."
        support = "Capture articles, docs, and notes without breaking flow."
        image = "save_webpage.png"
        layout = "left"
        primaryRect = @{ x = 70; y = 148; w = 648; h = 540 }
        textRect = @{ x = 760; y = 230; w = 510 }
        supportOffset = -2
        secondary = $null
    },
    @{
        id = "05-ask-to-memwyre"
        headline = "Ask MemWyre."
        support = "Get grounded answers from your saved context."
        image = "talk_to_knowledge.png"
        layout = "right"
        primaryRect = @{ x = 566; y = 168; w = 648; h = 540 }
        textRect = @{ x = 78; y = 204; w = 430 }
        supportOffset = -2
        secondary = $null
    },
    @{
        id = "06-cross-ai-post"
        headline = "Cross-post to any AI."
        support = "Continue in ChatGPT, Claude, or Gemini in one click."
        image = "cross-ai-post.png"
        layout = "left"
        primaryRect = @{ x = 70; y = 168; w = 648; h = 540 }
        textRect = @{ x = 760; y = 224; w = 420 }
        supportOffset = -2
        secondary = $null
    }
)

foreach ($slide in $slides) {
    $canvas = New-SlideCanvas -Width $CanvasWidth -Height $CanvasHeight -Colors $colors
    $bitmap = $canvas.bitmap
    $graphics = $canvas.graphics

    $headlineIconPath = $null
    if ($slide.ContainsKey("headlineIcon") -and -not [string]::IsNullOrWhiteSpace($slide.headlineIcon)) {
        $candidate = Join-Path $repoRoot $slide.headlineIcon
        if (Test-Path $candidate) {
            $headlineIconPath = $candidate
        }
    }

    $supportOffset = 4
    if ($slide.ContainsKey("supportOffset")) {
        $supportOffset = [float]$slide.supportOffset
    }

    if ($slide.ContainsKey("headlineLines")) {
        $headlineFontSize = if ($slide.ContainsKey("headlineFontSize")) { [float]$slide.headlineFontSize } else { 58.0 }
        $bodyFontSize = if ($slide.ContainsKey("bodyFontSize")) { [float]$slide.bodyFontSize } else { 38.0 }
        $lineAdvance = if ($slide.ContainsKey("lineAdvance")) { [float]$slide.lineAdvance } else { 82.0 }
        Draw-TitleOnlyLines -Graphics $graphics -Lines $slide.headlineLines -X $slide.textRect.x -Y $slide.textRect.y -Width $slide.textRect.w -Colors $colors -HeadlineIconPath $headlineIconPath -SupportLine $slide.support -SupportOffset $supportOffset -HeadlineFontSize $headlineFontSize -BodyFontSize $bodyFontSize -LineAdvance $lineAdvance
    } else {
        Draw-SlideText -Graphics $graphics -Headline $slide.headline -SupportLine $slide.support -X $slide.textRect.x -Y $slide.textRect.y -Width $slide.textRect.w -Colors $colors -HeadlineIconPath $headlineIconPath -SupportOffset $supportOffset
    }

    $outPath = Join-Path $outputDir ($slide.id + ".png")
    $imagePath = Join-Path $sourceDir $slide.image
    if (-not (Test-Path $imagePath)) {
        throw "Missing source image: '$imagePath'. All inputs must be in '$sourceDir'."
    }
    Assert-ValidSourceImage -ImagePath $imagePath -SlideId $slide.id

    $imageFull = [System.IO.Path]::GetFullPath($imagePath)
    $outputFull = [System.IO.Path]::GetFullPath($outputDir)
    $outputFullWithSep = $outputFull.TrimEnd('\') + '\'
    if (
        $imageFull.Equals($outputFull, [System.StringComparison]::OrdinalIgnoreCase) -or
        $imageFull.StartsWith($outputFullWithSep, [System.StringComparison]::OrdinalIgnoreCase)
    ) {
        throw "Loop guard: source image cannot be read from output directory ($outputDir). Move source files to '$sourceDir'."
    }
    Draw-SnapshotCard -Graphics $graphics -ImagePath $imagePath -Rect $slide.primaryRect -Colors $colors -Secondary $slide.secondary
    if ($slide.ContainsKey("extraCards")) {
        Draw-AdditionalCards -Graphics $graphics -Cards $slide.extraCards -SourceDir $sourceDir -Colors $colors
    }

    $bitmap.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

    $graphics.Dispose()
    $bitmap.Dispose()
}

$handoffPath = Join-Path $outputDir "figma_handoff.md"
$handoff = @"
# Extension Graphics — Figma Handoff Spec

## Canvas
- Size: 1280 x 800
- Frame count: 6
- Export: PNG

## Brand Tokens (Dark Mode)
- Background base: #1A1918
- Background depth: #24211F
- Surface: #2D2B2A
- Border: rgba(255,255,255,0.10)
- Heading: #FAF6F0
- Body text: #F2EEE8
- Accent: #D97757
- Highlight: #E8956E

## Shared Layout System
- Screenshot card radius: 24
- Glow layers: accent glow (top-right), highlight glow (bottom-left)

## Slide Specs
1. 01-capture-button
- Headline: Save AI responses and prompts with the [logo]
- Support: 
- Source: save_button.png
- Primary card: x=566, y=168, w=648, h=540
- Additional card: save_btn_2.png at x=86, y=470, w=360, h=152
- Secondary crop: none

2. 02-sync-button
- Headline: Tap [logo] button to sync your context to your knowledge base.
- Support: 
- Source: sync button.png
- Primary card: x=70, y=168, w=648, h=540
- Additional card: sync_btn.png at x=776, y=516, w=360, h=152
- Secondary crop: none

3. 03-mcp-server-connections
- Headline: Connect your AI stack with MCP.
- Support: Use your memory from Cursor, Claude, VS Code, and more.
- Source: mcp_connections.png
- Primary card: x=566, y=168, w=648, h=540
- Secondary crop: none

4. 04-save-from-any-webpage
- Headline: Save from any webpage.
- Support: Capture articles, docs, and notes without breaking flow.
- Source: save_webpage.png
- Primary card: x=70, y=168, w=648, h=540
- Secondary crop: none

5. 05-ask-to-memwyre
- Headline: Ask MemWyre.
- Support: Get grounded answers from your saved context.
- Source: talk_to_knowledge.png
- Primary card: x=566, y=168, w=648, h=540
- Secondary crop: none

6. 06-cross-ai-post
- Headline: Cross-post to any AI.
- Support: Continue in ChatGPT, Claude, or Gemini in one click.
- Source: cross-ai-post.png
- Primary card: x=70, y=168, w=648, h=540
- Secondary crop: none
"@

Set-Content -Path $handoffPath -Value $handoff -Encoding UTF8

$handoffJsonPath = Join-Path $outputDir "figma_handoff.json"
$handoffJson = @{
    canvas = @{
        width = 1280
        height = 800
        format = "png"
        count = 6
    }
    brandTokens = @{
        bgBase = "#1A1918"
        bgDepth = "#24211F"
        surface = "#2D2B2A"
        border = "rgba(255,255,255,0.10)"
        heading = "#FAF6F0"
        body = "#F2EEE8"
        accent = "#D97757"
        highlight = "#E8956E"
    }
    anchors = @{
        primaryCardRadius = 24
    }
    slides = @(
        @{
            id = "01-capture-button"
            source = "save_button.png"
            headline = "Save AI responses and prompts with the [logo]"
            support = ""
            headlineLines = @("Save AI", "responses and prompts", "with the [logo]")
            primary = @{ x = 566; y = 168; w = 648; h = 540 }
            headlineIcon = "extension/logo.png"
            extraCards = @(
                @{
                    image = "save_btn_2.png"
                    rect = @{ x = 86; y = 470; w = 360; h = 152 }
                }
            )
            secondary = $null
        },
        @{
            id = "02-sync-button"
            source = "sync button.png"
            headline = "Tap [logo] button to sync your context to your knowledge base."
            support = ""
            headlineLines = @("Tap [logo] button", "to sync your", "context to your", "knowledge base.")
            primary = @{ x = 70; y = 168; w = 648; h = 540 }
            headlineIcon = "extension/logo.png"
            extraCards = @(
                @{
                    image = "sync_btn.png"
                    rect = @{ x = 776; y = 516; w = 360; h = 152 }
                }
            )
            secondary = $null
        },
        @{
            id = "03-mcp-server-connections"
            source = "mcp_connections.png"
            headline = "Connect your AI stack with MCP."
            support = "Use your memory from Cursor, Claude, VS Code, and more."
            primary = @{ x = 566; y = 168; w = 648; h = 540 }
            secondary = $null
        },
        @{
            id = "04-save-from-any-webpage"
            source = "save_webpage.png"
            headline = "Save from any webpage."
            support = "Capture articles, docs, and notes without breaking flow."
            primary = @{ x = 70; y = 168; w = 648; h = 540 }
            secondary = $null
        },
        @{
            id = "05-ask-to-memwyre"
            source = "talk_to_knowledge.png"
            headline = "Ask MemWyre."
            support = "Get grounded answers from your saved context."
            primary = @{ x = 566; y = 168; w = 648; h = 540 }
            secondary = $null
        },
        @{
            id = "06-cross-ai-post"
            source = "cross-ai-post.png"
            headline = "Cross-post to any AI."
            support = "Continue in ChatGPT, Claude, or Gemini in one click."
            primary = @{ x = 70; y = 168; w = 648; h = 540 }
            secondary = $null
        }
    )
}

$handoffJson | ConvertTo-Json -Depth 8 | Set-Content -Path $handoffJsonPath -Encoding UTF8

$promoTilePath = Join-Path $outputDir "memwyre-promo-tile-440x280.png"
New-PromoTile -OutputPath $promoTilePath -LogoPath $logoPath -Colors $colors

Write-Output "Generated extension graphics in: $outputDir"
