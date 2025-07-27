rule auto_rule_20250727001510_2929 {
  strings:
    $o0 = "xA69u" wide ascii nocase
    $o1 = "_Iostream_error_category2" wide ascii nocase
    $o2 = "rdata" wide ascii nocase
  condition:
    3 of ($o*)
}