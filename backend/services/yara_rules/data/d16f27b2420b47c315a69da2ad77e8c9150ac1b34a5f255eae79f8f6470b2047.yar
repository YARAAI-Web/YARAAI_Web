rule auto_rule_20250727012910_6235 {
  strings:
    $o0 = "UnpackDDElParam" wide ascii nocase
    $o1 = "hsz2" wide ascii nocase
    $o2 = "pmbi" wide ascii nocase
    $o3 = "GetKeyNameTextW" wide ascii nocase
    $o4 = "DdeQueryConvInfo" wide ascii nocase
  condition:
    4 of ($o*)
}