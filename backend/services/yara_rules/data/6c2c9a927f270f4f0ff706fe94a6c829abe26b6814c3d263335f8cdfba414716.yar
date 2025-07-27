rule auto_rule_20250726095130_9874 {
  strings:
    $o0 = "dword_43B1DE" wide ascii nocase
    $o1 = "x411EFD00u" wide ascii nocase
    $o2 = "dword_43B577" wide ascii nocase
    $o3 = "dword_43B801" wide ascii nocase
    $o4 = "dword_43B384" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726095133_2463 {
  strings:
    $o0 = "dword_43B3A3" wide ascii nocase
    $o1 = "dword_43B8CA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726095138_0525 {
  condition:
    auto_rule_20250726095130_9874 or auto_rule_20250726095133_2463
}