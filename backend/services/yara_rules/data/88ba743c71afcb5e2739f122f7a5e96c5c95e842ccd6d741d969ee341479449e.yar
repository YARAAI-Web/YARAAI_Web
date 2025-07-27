rule auto_rule_20250727014056_2821 {
  strings:
    $o0 = "dbgrpt" wide ascii nocase
    $o1 = "_ftbuf" wide ascii nocase
    $o2 = "x101" wide ascii nocase
    $o3 = "word_446EF8" wide ascii nocase
  condition:
    4 of ($o*)
}