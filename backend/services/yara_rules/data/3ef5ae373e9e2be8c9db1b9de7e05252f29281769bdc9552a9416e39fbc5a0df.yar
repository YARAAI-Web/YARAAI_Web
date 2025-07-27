rule auto_rule_20250727043201_6909 {
  strings:
    $o0 = "stdenvp" wide ascii nocase
    $o1 = "x41C4u" wide ascii nocase
    $o2 = "InterlockedIncrement" wide ascii nocase
  condition:
    3 of ($o*)
}