rule auto_rule_20250726125922_7389 {
  strings:
    $o0 = "LoadMenuIndirectW" wide ascii nocase
    $o1 = "nIDStaticPath" wide ascii nocase
    $o2 = "pptDst" wide ascii nocase
    $o3 = "crKey" wide ascii nocase
  condition:
    4 of ($o*)
}