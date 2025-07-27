rule auto_rule_20250727014910_5759 {
  strings:
    $o0 = "CodePagea" wide ascii nocase
    $o1 = "byte_467B9C" wide ascii nocase
    $o2 = "dword_467D04" wide ascii nocase
    $o3 = "_CrtMemCheckpoint" wide ascii nocase
    $o4 = "_abnormal_termination" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727014913_0479 {
  strings:
    $o0 = "dword_467CD0" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727014917_8379 {
  condition:
    auto_rule_20250727014910_5759 or auto_rule_20250727014913_0479
}