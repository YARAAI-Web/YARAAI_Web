rule auto_rule_20250726203344_8591 {
  strings:
    $o0 = "dword_449ACC" wide ascii nocase
    $o1 = "dword_449D20" wide ascii nocase
    $o2 = "dword_449978" wide ascii nocase
    $o3 = "UnwindUp0_0" wide ascii nocase
    $o4 = "bound" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726203345_0674 {
  strings:
    $o0 = "x402044" wide ascii nocase
    $o1 = "dword_44994C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726203350_8288 {
  condition:
    auto_rule_20250726203344_8591 or auto_rule_20250726203345_0674
}