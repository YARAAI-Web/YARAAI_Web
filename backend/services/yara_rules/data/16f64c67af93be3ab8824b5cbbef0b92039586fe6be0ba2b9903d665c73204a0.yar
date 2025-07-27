rule auto_rule_20250727043417_7025 {
  strings:
    $o0 = "RemovePropW" wide ascii nocase
    $o1 = "lpLangGroupLocaleEnumProc" wide ascii nocase
  condition:
    all of them
}