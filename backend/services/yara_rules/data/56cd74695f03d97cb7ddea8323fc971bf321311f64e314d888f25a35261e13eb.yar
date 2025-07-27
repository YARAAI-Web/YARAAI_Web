rule auto_rule_20250727015918_9856 {
  strings:
    $o0 = "_d_inttype" wide ascii nocase
    $o1 = "_abstract_cw" wide ascii nocase
    $o2 = "word_418150" wide ascii nocase
  condition:
    3 of ($o*)
}