rule auto_rule_20250726122556_9107 {
  strings:
    $o0 = "dword_46ED68" wide ascii nocase
    $o1 = "dword_46E118" wide ascii nocase
    $o2 = "fill_dwords_with_EOS" wide ascii nocase
  condition:
    3 of ($o*)
}