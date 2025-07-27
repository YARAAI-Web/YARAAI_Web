rule auto_rule_20250726141740_7035 {
  strings:
    $o0 = "dword_409004" wide ascii nocase
    $o1 = "_fload_withFB" wide ascii nocase
  condition:
    all of them
}