rule auto_rule_20250726173546_2650 {
  strings:
    $o0 = "_setenvp" wide ascii nocase
    $o1 = "Runtime" wide ascii nocase
    $o2 = "x402560" wide ascii nocase
  condition:
    3 of ($o*)
}