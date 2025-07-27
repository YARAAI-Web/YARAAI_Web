rule auto_rule_20250726193636_9868 {
  strings:
    $o0 = "mallocgcSmallScanNoHeader" wide ascii nocase
    $o1 = "_ptr_atomic_Bool" wide ascii nocase
    $o2 = "runtime_mapclear" wide ascii nocase
    $o3 = "internal_abi__ptr_Type_IsDirectIface" wide ascii nocase
    $o4 = "reflectcallmove" wide ascii nocase
  condition:
    4 of ($o*)
}