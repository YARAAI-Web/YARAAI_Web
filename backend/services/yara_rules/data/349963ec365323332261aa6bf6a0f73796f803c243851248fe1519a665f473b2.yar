rule auto_rule_20250727012552_4550 {
  strings:
    $o0 = "byte_45C438" wide ascii nocase
    $o1 = "word_45D030" wide ascii nocase
    $o2 = "main_loop_0" wide ascii nocase
    $o3 = "x41C4u" wide ascii nocase
  condition:
    4 of ($o*)
}