rule auto_rule_20250726070522_8702 {
  strings:
    $o0 = "dword_469BA0" wide ascii nocase
    $o1 = "located" wide ascii nocase
    $o2 = "_un_inc" wide ascii nocase
    $o3 = "_CrtSetDbgFlag" wide ascii nocase
  condition:
    4 of ($o*)
}