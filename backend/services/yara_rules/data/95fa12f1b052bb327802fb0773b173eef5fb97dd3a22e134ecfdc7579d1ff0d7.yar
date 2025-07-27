rule auto_rule_20250726144625_4872 {
  strings:
    $o0 = "szUserMessage" wide ascii nocase
    $o1 = "dword_462028" wide ascii nocase
    $o2 = "_commit" wide ascii nocase
    $o3 = "_output" wide ascii nocase
    $o4 = "__sbh_alloc_new_group" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726144629_3891 {
  strings:
    $o0 = "Dumping" wide ascii nocase
    $o1 = "Client" wide ascii nocase
    $o2 = "byte_4654A0" wide ascii nocase
    $o3 = "_free_osfhnd" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726144632_1163 {
  condition:
    auto_rule_20250726144625_4872 or auto_rule_20250726144629_3891
}