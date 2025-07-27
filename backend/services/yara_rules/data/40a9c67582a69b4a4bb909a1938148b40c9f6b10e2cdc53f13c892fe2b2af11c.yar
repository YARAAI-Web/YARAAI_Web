rule auto_rule_20250726184847_0639 {
  strings:
    $o0 = "x7657564u" wide ascii nocase
    $o1 = "dword_40A520" wide ascii nocase
    $o2 = "ReadIntervalTimeout" wide ascii nocase
    $o3 = "dword_40A6F8" wide ascii nocase
    $o4 = "dword_40A5B0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726184850_8706 {
  strings:
    $o0 = "dword_41002F" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726184855_9571 {
  condition:
    auto_rule_20250726184847_0639 or auto_rule_20250726184850_8706
}