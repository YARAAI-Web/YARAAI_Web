rule auto_rule_20250726122243_6761 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "_ctype" wide ascii nocase
    $o2 = "dword_46444C" wide ascii nocase
    $o3 = "CrtMessageWindow" wide ascii nocase
    $o4 = "dword_4643E0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726122247_6824 {
  strings:
    $o0 = "_pLastBlock" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726122252_2927 {
  condition:
    auto_rule_20250726122243_6761 or auto_rule_20250726122247_6824
}