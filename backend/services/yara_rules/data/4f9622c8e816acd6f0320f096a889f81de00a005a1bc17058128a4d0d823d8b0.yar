rule auto_rule_20250726085056_3990 {
  strings:
    $o0 = "off_4292B4" wide ascii nocase
    $o1 = "dword_4294D0" wide ascii nocase
    $o2 = "x2040" wide ascii nocase
    $o3 = "dword_4294F8" wide ascii nocase
    $o4 = "dword_42950C" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726085059_2063 {
  strings:
    $o0 = "x5C72" wide ascii nocase
    $o1 = "BC8h" wide ascii nocase
    $o2 = "off_4298E9" wide ascii nocase
    $o3 = "word_42970C" wide ascii nocase
    $o4 = "dword_429570" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726085102_9250 {
  strings:
    $o0 = "xFF5F" wide ascii nocase
    $o1 = "x774500002646LL" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726085113_7428 {
  condition:
    (auto_rule_20250726085056_3990 and auto_rule_20250726085059_2063) or (auto_rule_20250726085056_3990 and auto_rule_20250726085102_9250) or (auto_rule_20250726085059_2063 and auto_rule_20250726085102_9250)
}