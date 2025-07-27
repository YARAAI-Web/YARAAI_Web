rule auto_rule_20250726070651_9755 {
  strings:
    $o0 = "DlgDirSelectExW" wide ascii nocase
    $o1 = "hRecipient" wide ascii nocase
    $o2 = "fInherit" wide ascii nocase
    $o3 = "CreateDialogParamA" wide ascii nocase
    $o4 = "pqosPrev" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726070654_5198 {
  strings:
    $o0 = "lpptBuf" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726070659_7359 {
  condition:
    auto_rule_20250726070651_9755 or auto_rule_20250726070654_5198
}