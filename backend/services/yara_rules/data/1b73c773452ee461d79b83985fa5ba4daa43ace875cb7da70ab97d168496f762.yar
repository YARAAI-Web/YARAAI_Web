rule auto_rule_20250726162157_0796 {
  strings:
    $o0 = "dword_44A03C" wide ascii nocase
    $o1 = "dword_449EC4" wide ascii nocase
    $o2 = "CPtoLCID" wide ascii nocase
    $o3 = "dword_44A2A0" wide ascii nocase
    $o4 = "dword_449EB0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726162200_9730 {
  strings:
    $o0 = "x402811" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726162203_5559 {
  condition:
    auto_rule_20250726162157_0796 or auto_rule_20250726162200_9730
}