rule auto_rule_20250726180039_9412 {
  strings:
    $o0 = "asc_404034" wide ascii nocase
    $o1 = "lpClassName" wide ascii nocase
    $o2 = "byte_404456" wide ascii nocase
    $o3 = "FileA" wide ascii nocase
    $o4 = "NewFileName" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726180042_4501 {
  strings:
    $o0 = "dword_407519" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726180047_4345 {
  condition:
    auto_rule_20250726180039_9412 or auto_rule_20250726180042_4501
}