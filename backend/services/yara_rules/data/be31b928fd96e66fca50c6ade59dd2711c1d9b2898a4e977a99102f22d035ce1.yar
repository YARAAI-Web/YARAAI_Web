rule auto_rule_20250726204022_5690 {
  strings:
    $o0 = "x1208" wide ascii nocase
    $o1 = "qword_429584" wide ascii nocase
    $o2 = "x4F2B" wide ascii nocase
    $o3 = "dword_429544" wide ascii nocase
    $o4 = "BBCh" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726204025_7187 {
  strings:
    $o0 = "x442" wide ascii nocase
    $o1 = "x2545" wide ascii nocase
    $o2 = "dword_4294D8" wide ascii nocase
    $o3 = "xFF5F" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726204029_2170 {
  condition:
    auto_rule_20250726204022_5690 or auto_rule_20250726204025_7187
}