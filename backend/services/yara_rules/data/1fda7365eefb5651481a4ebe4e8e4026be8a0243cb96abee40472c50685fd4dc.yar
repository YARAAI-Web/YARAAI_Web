rule auto_rule_20250726070055_5000 {
  strings:
    $o0 = "off_4290FC" wide ascii nocase
    $o1 = "dword_429941" wide ascii nocase
    $o2 = "word_429724" wide ascii nocase
    $o3 = "xDFF1423" wide ascii nocase
    $o4 = "xFFFFACD7" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726070059_3728 {
  strings:
    $o0 = "x728Cu" wide ascii nocase
    $o1 = "dword_429644" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726070104_3611 {
  condition:
    auto_rule_20250726070055_5000 or auto_rule_20250726070059_3728
}