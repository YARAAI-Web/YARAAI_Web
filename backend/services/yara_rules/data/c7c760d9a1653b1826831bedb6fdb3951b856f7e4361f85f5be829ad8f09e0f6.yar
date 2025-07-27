rule auto_rule_20250726222202_7460 {
  strings:
    $o0 = "x2A17" wide ascii nocase
    $o1 = "x7943u" wide ascii nocase
    $o2 = "xBC0u" wide ascii nocase
    $o3 = "x8309" wide ascii nocase
    $o4 = "x8601u" wide ascii nocase
  condition:
    4 of ($o*)
}