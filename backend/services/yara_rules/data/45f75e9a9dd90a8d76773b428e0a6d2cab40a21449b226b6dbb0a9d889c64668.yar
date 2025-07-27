rule auto_rule_20250726221618_3287 {
  strings:
    $o0 = "_allshl" wide ascii nocase
    $o1 = "dword_46A0BC" wide ascii nocase
    $o2 = "lpCharType" wide ascii nocase
    $o3 = "_cinit" wide ascii nocase
    $o4 = "dword_469CFC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726221622_9999 {
  strings:
    $o0 = "dword_4698E8" wide ascii nocase
    $o1 = "doexit" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726221627_2143 {
  condition:
    auto_rule_20250726221618_3287 or auto_rule_20250726221622_9999
}