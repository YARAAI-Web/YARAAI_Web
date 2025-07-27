rule auto_rule_20250726225859_9675 {
  strings:
    $o0 = "byte_4C160C" wide ascii nocase
    $o1 = "byte_4BB568" wide ascii nocase
    $o2 = "byte_4C10C5" wide ascii nocase
  condition:
    3 of ($o*)
}