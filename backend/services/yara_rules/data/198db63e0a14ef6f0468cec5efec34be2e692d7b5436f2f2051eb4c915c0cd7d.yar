rule auto_rule_20250726082846_2344 {
  strings:
    $o0 = "word_4227CE" wide ascii nocase
    $o1 = "dword_42E8D9" wide ascii nocase
    $o2 = "dword_42D020" wide ascii nocase
    $o3 = "dword_42E731" wide ascii nocase
    $o4 = "x55D9E7AB" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726082849_3804 {
  strings:
    $o0 = "x63C18612" wide ascii nocase
    $o1 = "xD06457F2" wide ascii nocase
    $o2 = "x69B100005ECDLL" wide ascii nocase
    $o3 = "dword_42D038" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726082855_9459 {
  condition:
    auto_rule_20250726082846_2344 or auto_rule_20250726082849_3804
}