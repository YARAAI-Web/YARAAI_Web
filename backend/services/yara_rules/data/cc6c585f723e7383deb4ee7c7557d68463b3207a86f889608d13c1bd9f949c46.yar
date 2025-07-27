rule auto_rule_20250727005149_7685 {
  strings:
    $o0 = "strncnt" wide ascii nocase
    $o1 = "fill_dwords_with_EOS" wide ascii nocase
    $o2 = "off_449574" wide ascii nocase
    $o3 = "_except_handler3" wide ascii nocase
  condition:
    4 of ($o*)
}