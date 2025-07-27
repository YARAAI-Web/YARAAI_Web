rule auto_rule_20250726074528_1419 {
  strings:
    $o0 = "Unhandled" wide ascii nocase
    $o1 = "wtempnam" wide ascii nocase
    $o2 = "qword_140042E08" wide ascii nocase
    $o3 = "referenced" wide ascii nocase
  condition:
    4 of ($o*)
}