rule auto_rule_20250726162806_8303 {
  strings:
    $o0 = "fill_dwords_with_EOS" wide ascii nocase
    $o1 = "main_loop_1" wide ascii nocase
    $o2 = "dword_460750" wide ascii nocase
  condition:
    3 of ($o*)
}