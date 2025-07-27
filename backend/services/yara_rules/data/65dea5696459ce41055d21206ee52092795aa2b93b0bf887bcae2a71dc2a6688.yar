rule auto_rule_20250727011356_3815 {
  strings:
    $o0 = "dword_43B08A" wide ascii nocase
    $o1 = "dword_43B30A" wide ascii nocase
    $o2 = "dword_43B754" wide ascii nocase
    $o3 = "dword_43B56A" wide ascii nocase
    $o4 = "x36933000" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727011359_6958 {
  strings:
    $o0 = "x44DE5E00u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727011402_5425 {
  condition:
    auto_rule_20250727011356_3815 or auto_rule_20250727011359_6958
}