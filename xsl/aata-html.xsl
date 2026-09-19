<?xml version="1.0" encoding="UTF-8"?>

<!-- AATA-specific HTML localization fixes for the PreTeXt web output. -->
<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="1.0">

  <xsl:import href="../xsl/pretext-html.xsl"/>

  <!-- PreTeXt 2.44.0 hard-codes these two search-field strings in English. -->
  <xsl:template name="native-search-results">
    <xsl:if test="$has-native-search">
      <dialog id="ptx-search-dialog" class="ptx-dialog ptx-search-dialog">
        <xsl:variable name="close-localization">
          <xsl:apply-templates select="." mode="type-name">
            <xsl:with-param name="string-id" select="'close'"/>
          </xsl:apply-templates>
        </xsl:variable>
        <div class="ptx-search-dialog-controls">
          <input aria-label="Termo de pesquisa" id="ptx-search-terms" class="ptx-search-terms" type="text" name="terms" placeholder="Termos de pesquisa"/>
          <button aria-label="{$close-localization}" id="ptx-search-close" class="ptx-search-close">
            <xsl:call-template name="insert-symbol">
              <xsl:with-param name="name" select="'close'"/>
            </xsl:call-template>
          </button>
        </div>
        <div id="ptx-search-status" class="ptx-search-status" aria-live="polite" aria-atomic="true">
        </div>
        <h2 class="heading ptx-search-results-heading">
          <xsl:apply-templates select="." mode="type-name">
            <xsl:with-param name="string-id" select="'search-results-heading'"/>
          </xsl:apply-templates>
          <xsl:text>: </xsl:text>
        </h2>
        <div id="ptx-search-empty" class="ptx-search-empty">
          <span>
            <xsl:apply-templates select="." mode="type-name">
              <xsl:with-param name="string-id" select="'no-search-results'"/>
            </xsl:apply-templates>
            <xsl:text>.</xsl:text>
          </span>
        </div>
        <ol id="ptx-search-results" class="ptx-search-results">
        </ol>
      </dialog>
    </xsl:if>
  </xsl:template>

</xsl:stylesheet>
