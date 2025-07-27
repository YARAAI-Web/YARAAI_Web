rule auto_rule_20250726233508_4842 {
  strings:
    $o0 = "word_429724" wide ascii nocase
    $o1 = "x4040" wide ascii nocase
    $o2 = "x7F7Fu" wide ascii nocase
    $o3 = "x6BBDu" wide ascii nocase
    $o4 = "dword_4298C1" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726233511_7764 {
  strings:
    $o0 = "x73F7" wide ascii nocase
    $o1 = "x5E75u" wide ascii nocase
    $o2 = "x6807" wide ascii nocase
    $o3 = "BF8h" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726233515_3441 {
  condition:
    auto_rule_20250726233508_4842 or auto_rule_20250726233511_7764
}