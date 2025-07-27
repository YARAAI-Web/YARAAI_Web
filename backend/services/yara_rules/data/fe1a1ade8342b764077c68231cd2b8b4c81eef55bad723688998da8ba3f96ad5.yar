rule auto_rule_20250726075945_1958 {
  strings:
    $o0 = "x3BD9u" wide ascii nocase
    $o1 = "dword_40A744" wide ascii nocase
    $o2 = "x1BC7CE72" wide ascii nocase
    $o3 = "dword_40A54C" wide ascii nocase
    $o4 = "word_40A774" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726075948_8779 {
  strings:
    $o0 = "x1810" wide ascii nocase
    $o1 = "dword_40A168" wide ascii nocase
    $o2 = "off_40A15C" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726075951_9891 {
  condition:
    auto_rule_20250726075945_1958 or auto_rule_20250726075948_8779
}