rule auto_rule_20250726103459_2507 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "byte_450E9C" wide ascii nocase
    $o2 = "UnwindUp1_0" wide ascii nocase
    $o3 = "__freetlocinfo" wide ascii nocase
    $o4 = "dword_4507E0" wide ascii nocase
  condition:
    4 of ($o*)
}