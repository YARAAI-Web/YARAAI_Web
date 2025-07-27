rule auto_rule_20250726144855_6437 {
  strings:
    $o0 = "write_char" wide ascii nocase
    $o1 = "dbgrpt" wide ascii nocase
    $o2 = "Offset" wide ascii nocase
  condition:
    3 of ($o*)
}