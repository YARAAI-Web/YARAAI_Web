rule auto_rule_20250726071432_6389 {
  strings:
    $o0 = "dword_4657CC" wide ascii nocase
    $o1 = "_CrtMemCheckpoint" wide ascii nocase
    $o2 = "byte_463B00" wide ascii nocase
    $o3 = "dword_46399C" wide ascii nocase
    $o4 = "byte_460DF0" wide ascii nocase
  condition:
    4 of ($o*)
}