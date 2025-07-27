rule auto_rule_20250726071246_5763 {
  strings:
    $o0 = "lprcItem" wide ascii nocase
    $o1 = "pSrc" wide ascii nocase
    $o2 = "GetInputDesktop" wide ascii nocase
  condition:
    3 of ($o*)
}