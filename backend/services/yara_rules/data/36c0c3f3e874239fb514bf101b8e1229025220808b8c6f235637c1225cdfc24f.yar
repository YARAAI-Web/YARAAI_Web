rule auto_rule_20250726070420_1889 {
  strings:
    $o0 = "_CrtSetDbgFlag" wide ascii nocase
    $o1 = "Chance" wide ascii nocase
    $o2 = "byte_40DCA0" wide ascii nocase
    $o3 = "dword_467CBC" wide ascii nocase
  condition:
    4 of ($o*)
}