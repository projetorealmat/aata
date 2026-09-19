<?xml version="1.0" encoding="UTF-8"?>

<!-- AATA-specific PDF fallback for environments without Inconsolata OTF files. -->
<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="1.0">

  <xsl:import href="../xsl/pretext-latex.xsl"/>

  <!-- Keep Inconsolata when installed; otherwise use the bundled Latin Modern Mono. -->
  <xsl:template name="font-xelatex-mono">
    <xsl:if test="$b-needs-mono-font">
      <xsl:text>\IfFontExistsTF{Inconsolatazi4-Regular.otf}{%&#xa;</xsl:text>
      <xsl:text>  \IfFontExistsTF{Inconsolatazi4-Bold.otf}{%&#xa;</xsl:text>
      <xsl:text>    \usepackage{zi4}&#xa;</xsl:text>
      <xsl:text>    \setmonofont[BoldFont=Inconsolatazi4-Bold.otf,StylisticSet={1,3}]{Inconsolatazi4-Regular.otf}&#xa;</xsl:text>
      <xsl:text>  }{%&#xa;</xsl:text>
      <xsl:text>    \setmonofont{Latin Modern Mono}&#xa;</xsl:text>
      <xsl:text>  }&#xa;</xsl:text>
      <xsl:text>}{%&#xa;</xsl:text>
      <xsl:text>  \setmonofont{Latin Modern Mono}&#xa;</xsl:text>
      <xsl:text>}&#xa;</xsl:text>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
