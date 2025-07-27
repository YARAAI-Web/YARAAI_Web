rule auto_rule_20250726110115_2804 {
  strings:
    $o0 = "dword_4643D4" wide ascii nocase
    $o1 = "_CrtMemDumpAllObjectsSince" wide ascii nocase
    $o2 = "_aullrem" wide ascii nocase
  condition:
    3 of ($o*)
}