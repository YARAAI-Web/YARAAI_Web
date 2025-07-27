rule auto_rule_20250727001944_9717 {
  strings:
    $o0 = "aSceAxwhb9imi" wide ascii nocase
    $o1 = "x421Eu" wide ascii nocase
    $o2 = "x673F" wide ascii nocase
    $o3 = "off_41D25C" wide ascii nocase
  condition:
    4 of ($o*)
}