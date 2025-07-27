rule auto_rule_20250726111900_8238 {
  strings:
    $o0 = "_cpinfo" wide ascii nocase
    $o1 = "GetActiveWindow_0" wide ascii nocase
    $o2 = "_CrtSetDbgFlag" wide ascii nocase
    $o3 = "byte_465981" wide ascii nocase
  condition:
    4 of ($o*)
}