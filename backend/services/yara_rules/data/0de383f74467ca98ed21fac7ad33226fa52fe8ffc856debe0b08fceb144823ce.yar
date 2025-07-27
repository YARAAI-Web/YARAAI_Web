rule auto_rule_20250726153649_0877 {
  strings:
    $o0 = "_wincmdln" wide ascii nocase
    $o1 = "lpCharType" wide ascii nocase
    $o2 = "dword_40CFDC" wide ascii nocase
    $o3 = "__sbh_alloc_new_group" wide ascii nocase
    $o4 = "dword_40C588" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726153652_1659 {
  strings:
    $o0 = "CPtoLCID" wide ascii nocase
    $o1 = "off_40C57C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726153655_9355 {
  condition:
    auto_rule_20250726153649_0877 or auto_rule_20250726153652_1659
}