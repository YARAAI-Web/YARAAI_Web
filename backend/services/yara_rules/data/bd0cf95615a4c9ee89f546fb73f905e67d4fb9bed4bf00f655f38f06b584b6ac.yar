rule auto_rule_20250727022657_4921 {
  strings:
    $o0 = "x41C4u" wide ascii nocase
    $o1 = "pmxcd" wide ascii nocase
    $o2 = "_global_unwind2" wide ascii nocase
    $o3 = "doexit" wide ascii nocase
    $o4 = "VirtualFree" wide ascii nocase
  condition:
    5 of ($o*)
}