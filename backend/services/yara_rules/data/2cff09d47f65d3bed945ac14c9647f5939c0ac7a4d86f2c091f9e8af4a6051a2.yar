rule auto_rule_20250726232757_0845 {
  strings:
    $o0 = "byte_73B50" wide ascii nocase
    $o1 = "byte_1E108" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}