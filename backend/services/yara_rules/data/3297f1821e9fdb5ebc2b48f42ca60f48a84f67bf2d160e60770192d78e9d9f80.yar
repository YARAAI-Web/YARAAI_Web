rule auto_rule_20250727001759_1287 {
  strings:
    $o0 = "_mtdeletelocks" wide ascii nocase
    $o1 = "__sbh_alloc_new_region" wide ascii nocase
    $o2 = "dword_454B48" wide ascii nocase
    $o3 = "_aulldvrm" wide ascii nocase
    $o4 = "dword_46EC28" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727001802_6960 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "dword_46E280" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727001804_1771 {
  condition:
    auto_rule_20250727001759_1287 or auto_rule_20250727001802_6960
}