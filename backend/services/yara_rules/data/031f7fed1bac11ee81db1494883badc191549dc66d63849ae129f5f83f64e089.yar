rule auto_rule_20250727034013_1980 {
  strings:
    $o0 = "dword_40A67C" wide ascii nocase
    $o1 = "x301A" wide ascii nocase
    $o2 = "dword_4100C7" wide ascii nocase
    $o3 = "xAF2B8DF8DBADC697uLL" wide ascii nocase
    $o4 = "x1A5A" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727034016_6055 {
  strings:
    $o0 = "x7144" wide ascii nocase
    $o1 = "x1D12u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727034020_4844 {
  condition:
    auto_rule_20250727034013_1980 or auto_rule_20250727034016_6055
}